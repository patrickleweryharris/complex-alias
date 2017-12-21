#!/bin/bash

GOLDENDIR="$HOME/.complex-alias"

echo "Installing to $GOLDENDIR ..."
mkdir $GOLDENDIR
chmod +x complex-alias
chmod +x script-maker.py
cp complex-alias $GOLDENDIR/complex-alias
cp script-maker.py $GOLDENDIR/script-maker.py
echo "Installation complete. Make sure to add $GOLDENDIR to your PATH"
