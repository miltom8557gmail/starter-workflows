#!/bin/bash
# Altera a cor principal no index.html dinamicamente
sed -i "s/#00ffcc//g" templates/index.html
sed -i "s/#ff003c//g" templates/index.html
echo "Interface personalizada para "
