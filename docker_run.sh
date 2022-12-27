#!/bin/bash
# Copyright 2022 Xilinx Inc.

confirm() {
  echo -en "\n\nDo you agree to the terms and wish to proceed [y/n]? "
  read REPLY
  case $REPLY in
    [Yy]) ;;
    [Nn]) exit 0 ;;
    *) confirm ;;
  esac
    REPLY=''
}


if [[ ! -f ".confirm" ]]; then

  sed -n '1, 5p' ./docker/dockerfiles/PROMPT.txt
  read -n 1 -s -r -p "Press any key to continue..." key

  sed -n '5, 15p' ./docker/dockerfiles/PROMPT.txt
  read -n 1 -s -r -p "Press any key to continue..." key

  sed -n '15, 28p' ./docker/dockerfiles/PROMPT.txt
  read -n 1 -s -r -p "Press any key to continue..." key

  sed -n '28, 61p' ./docker/dockerfiles/PROMPT.txt
  read -n 1 -s -r -p "Press any key to continue..." key

  sed -n '62, 224p' ./docker/dockerfiles/PROMPT.txt
  read -n 1 -s -r -p "Press any key to continue..." key

  sed -n '224, 308p' ./docker/dockerfiles/PROMPT.txt
  read -n 1 -s -r -p "Press any key to continue..." key

  sed -n '309, 520p' ./docker/dockerfiles/PROMPT.txt
  read -n 1 -s -r -p "Press any key to continue..." key
  
  confirm
fi

if [[ "$1" == "-h" || "$1" == "--help" ]]; then
    echo "Usage: $0 <image>"
    exit 2
fi

HERE=$(pwd -P) # Absolute path of current directory
user=`whoami`
uid=`id -u`
gid=`id -g`

DOCKER_REPO="xilinx/"

BRAND=vitis-ai
VERSION=latest

CPU_IMAGE_TAG=${DOCKER_REPO}${BRAND}-cpu:${VERSION}
GPU_IMAGE_TAG=${DOCKER_REPO}${BRAND}-gpu:${VERSION}
IMAGE_NAME="${1:-$CPU_IMAGE_TAG}"
DEFAULT_COMMAND="bash"

if [[ $# -gt 0 ]]; then
  shift 1;
  DEFAULT_COMMAND="$@"
  if [[ -z "$1" ]]; then
    DEFAULT_COMMAND="bash"
  fi
fi

DETACHED="-it"

xclmgmt_driver="$(find /dev -name xclmgmt\*)"
docker_devices=""
for i in ${xclmgmt_driver} ;
do
  docker_devices+="--device=$i "
done

render_driver="$(find /dev/dri -name renderD\*)"
for i in ${render_driver} ;
do
  docker_devices+="--device=$i "
done

DOCKER_RUN_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
if [ "$HERE" != "$DOCKER_RUN_DIR" ]; then
  echo "WARNING: Please start 'docker_run.sh' from the Vitis-AI/ source directory";
fi

docker_run_params=$(cat <<-END
    -v /dev/shm:/dev/shm \
    -v /opt/xilinx/dsa:/opt/xilinx/dsa \
    -v /opt/xilinx/overlaybins:/opt/xilinx/overlaybins \
    -e USER=$user -e UID=$uid -e GID=$gid \
    -e VERSION=$VERSION \
    -v $DOCKER_RUN_DIR:/vitis_ai_home \
    -v $HERE:/workspace \
    -w /workspace \
    --network=host \
    ${DETACHED} \
    ${RUN_MODE} \
    $IMAGE_NAME \
    $DEFAULT_COMMAND
END
)

##############################
touch .confirm 
if [[ $IMAGE_NAME == *"gpu"* ]]; then
  docker run \
    $docker_devices \
    --gpus all \
    $docker_run_params
else
  docker run \
    $docker_devices \
    $docker_run_params
fi
