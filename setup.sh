#!/usr/bin/env bash

# -e If a command fails, set -e will make the whole script exit, instead of just resuming on the next line.
# -f Disable filename expansion (globbing) upon seeing *, ?, etc.
# see https://www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html
SET_FLAGS='ef'
set -${SET_FLAGS}

#
# Run me using `. setup.sh`
# Don't run me in any other way, I won't work!
#

#
# INSTALL CONDA
#
if conda > /dev/null; then
    echo "Conda installed."
else
  echo 'Conda not detected. Installing conda...'
  unameOut="$(uname -s)"
  case "${unameOut}" in
    Linux*)
        echo 'Installing conda for Linux...'
        unset PYTHONPATH
        curl -o ~/miniconda-install.sh https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh
        bash ~/miniconda-install.sh -bfp /usr/local
        rm -f ~/miniconda-install.sh
        conda init bash
        source $HOME/.bashrc
        ;;
    Darwin*)
        echo 'Installing conda for MacOS...'
        curl -o ~/miniconda-install.sh https://repo.continuum.io/miniconda/Miniconda2-latest-MacOSX-x86_64.sh
        chmod +x ~/miniconda-install.sh
        ~/miniconda-install.sh -b
        rm -f ~/miniconda-install.sh
        echo ". \$HOME/miniconda2/etc/profile.d/conda.sh" >> ~/.bash_profile
        . $HOME/.bash_profile
        ;;
    *)
        echo 'ERROR: OS not supported (only Linux and MacOS). Please install conda/miniconda manually and re-run the script.' >> /dev/stderr
        exit 1
  esac
fi

#
# INSTALL 'ej-card-game-backend' ENVIRONMENT WITH ALL DEPENDENCIES
#
if conda activate ej-card-game-backend; then
   echo -e "Anaconda 'ej-card-game-backend' environment detected."
else
   #
   # INSTALL DEPENDENCIES
   #
   echo -e "Anaconda 'ej-card-game-backend' environment not detected.\nInstalling anaconda environment 'ej-card-game-backend' together with all the required dependencies..."
   conda env create -f environment.yml
   conda activate ej-card-game-backend
   mkdir -p "$CONDA_PREFIX/etc/conda/activate.d"
   #
   # $PYTHONPATH CONFIGURATION
   #
   touch "$CONDA_PREFIX/etc/conda/activate.d/python_path.sh"
   echo "export PYTHONPATH=$PWD" > "$CONDA_PREFIX/etc/conda/activate.d/python_path.sh"
   chmod +x "$CONDA_PREFIX/etc/conda/activate.d/python_path.sh"

   #
   # ACTIVATE CONFIGURATIONS
   #
   conda deactivate
   conda activate ej-card-game-backend
   echo "Run 'conda activate ej-card-game-backend' to enable python virtual environment to run the scripts."
fi;

# disable all the previously set flags to allow for normal shell use
set +${SET_FLAGS}
