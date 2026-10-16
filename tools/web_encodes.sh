#!/bin/bash
# Web-delivery encodes of the trailers: longest side 1280, CRF 26.
#
# The masters are ~30 MB each at 8 Mbps because film grain is incompressible.
# At viewing size 720p/CRF 26 is indistinguishable from the master -- compared
# side by side before choosing it -- and lands around 6 MB. Denoising at 1080p
# was tried and gained nothing; -tune grain made it worse, which is its job.
set -u
cd "$(dirname "$0")/.."
IN=promo
OUT=promo/web
mkdir -p "$OUT"
for f in "$IN"/*.mp4; do
  b=$(basename "$f" .mp4)
  case "$b" in
    *-vertical) sc="720:1280" ;;
    *-square)   sc="720:720"  ;;
    *)          sc="1280:720" ;;
  esac
  ffmpeg -v error -y -i "$f" -vf "scale=$sc" \
    -c:v libx264 -preset slow -crf 26 -pix_fmt yuv420p -movflags +faststart \
    -c:a aac -b:a 128k "$OUT/$b.mp4" \
    && echo "ok   $b  $(du -h "$OUT/$b.mp4" | cut -f1)" \
    || echo "FAIL $b"
done
echo "ALL DONE"
