#!/bin/bash
# Publish the trailer page, its posters and the web encodes to the VPS.
#
# The page lives at /trailers/contingency-2027/ and NOT under /conventions/,
# which is behind auth_basic -- a password box is right for scenario material
# and fatal for an advert. The flyer prints this URL, so it must stay public.
#
# rsync writes files as root:root; nginx serves them because 644 is world
# readable, but the house convention here is webftp:www-data, so chown after.
set -euo pipefail
cd "$(dirname "$0")/.."
HOST=foundry
DEST=/var/www/web.oneoffgames.com/trailers/contingency-2027

python3 tools/build_trailer_site.py

echo "--> page and posters"
rsync -rt --no-perms web/trailers/index.html web/trailers/posters "$HOST:$DEST/"
echo "--> web encodes"
rsync -rt --no-perms promo/web/ "$HOST:$DEST/"

ssh "$HOST" "cd $DEST && chown -R webftp:www-data . && chmod 644 *.mp4 index.html posters/*.jpg && chmod 755 . posters"

echo "--> verifying"
B=https://web.oneoffgames.com/trailers/contingency-2027
code=$(curl -s -o /dev/null -w '%{http_code}' --max-time 20 "$B/")
[ "$code" = 200 ] || { echo "FAIL: index returned $code"; exit 1; }
bad=0
for f in $(curl -s --max-time 20 "$B/" | grep -oE '(src|href)="[a-z0-9./-]+\.(mp4|jpg)"' | sed 's/.*="//;s/"//' | sort -u); do
  c=$(curl -s -o /dev/null -w '%{http_code}' --max-time 20 -r 0-255 "$B/$f")
  case "$c" in 200|206) ;; *) echo "BROKEN $c $f"; bad=$((bad+1));; esac
done
[ "$bad" = 0 ] || { echo "FAIL: $bad broken links"; exit 1; }
echo "OK: $B/ is live, every asset resolves"
