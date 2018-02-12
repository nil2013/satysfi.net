#!/bin/bash

# ファイル名の生成
uuid=$(uuidgen)
filename=/tmp/satysfi.net/demo/${uuid}.saty
if [ -z "$HOME" ]; then
    export HOME=/home/satysfi/
fi

# opam設定読み込み
source $HOME/.opam/opam-init/init.sh

# satysfi周辺ファイル配置
mkdir -p /tmp/satysfi.net/
cp -r $(dirname $0)/demo/ /tmp/satysfi.net/demo/

# 入力satysfiファイル配置
echo "$1" > ${filename}

# コンパイル
cd /tmp/satysfi.net/demo
satysfi --version
satysfi ${filename} 2>&1

# ファイル名表示(stderr)
echo ${uuid} 1>&2
