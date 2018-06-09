# Siri Multirotor Soundpack for OpenTX
## Description

This repository contains an OpenTX soundpack which was generated using the
Samantha (Siri) voice of Apple's text-to-speech engine.  It is compatible with
OpenTX 2.2 and was tested on the Taranis X9D and Q X7.

The phrases provided by this soundpack fall into one of three categories:
 * OpenTX system messages
 * Multirotor related
 * Funny lines

## Download & Install

Go to the releases page and download the latest ZIP archive. Delete the
`SOUNDS/en/` directory on your OpenTX SD card. Extract the archive and copy
its contents to the `SOUNDS/` directory of the SD card.

## Technical Details

The file `index.csv` contains the database of all messages. Python scripts in
the `tools/` directory are used to process this data using text-to-speech. The
CSV file uses the following columns:

 * `_idx` filename from which this message was originally extracted
 * `_category` original category assigned to this message
 * `category` new category assigned to this message
 * `directory` file system path to store this message in
 * `_filename` original filename of this message
 * `filename` new filename of this message
 * `_text` spoken words of the message

## Credits

* Inspiration: "Amber" sound pack by Arron Bates (theKM)
* Original "taranis-siri-sound-pack" by: Dale Higgs (dale3h)
* Improved by: Philip Huppert (Phaeilo)

