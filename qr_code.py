#!/usr/bin/env python3

import qrcode
import qrcode.image.svg


def main():
    url = 'https://diana-hep.org/pyhf'
    factory = qrcode.image.svg.SvgFillImage
    img = qrcode.make(url, image_factory=factory)
    img.save('figures/qr_code.svg')


if __name__ == '__main__':
    main()
