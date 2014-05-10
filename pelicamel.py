#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os
import sys
import codecs
import shutil
import argparse

parser = argparse.ArgumentParser(description='Process a directory of Pelican-style Markdown and create Camel-style nested directories.')
parser.add_argument(
  '-s',
  '--source',
  nargs=1,
  help='Source directory containing Pelican-style *.md files.')
parser.add_argument(
  '-d',
  '--destination',
  nargs=1,
  help='Root directory to create subdirectories and files it.')
args = parser.parse_args()

originDir = args.source[0]

rootDestDir = args.destination[0]

currentDirList = os.listdir(originDir)

def safeMkDir(f):
    d = f
    if not os.path.exists(d):
        os.makedirs(d)

def convertMmdMeta(mmdfile):
  f = codecs.open(mmdfile,'r','utf-8')
  camelMetaList = []
  content = f.read()
  content = content.replace('\r','\n')
  contentBlocks = content.split('\n\n')
  headBlock = contentBlocks[0]
  headLines = headBlock.splitlines()
  for hl in headLines:
    if ':' in hl:
      hl = hl.split(':')
      key = hl[0].strip()
      value = hl[1].strip()
      newLine = '@@ ' + key + '=' + value
      camelMetaList.append(newLine)
    else:
      print('WARNING! NO MMD METADATA TO CONVERT!')
  if len(camelMetaList) > 0:
    camelMetaBlock = '\n'.join(camelMetaList) + '\n\n'
    content = camelMetaBlock + '\n\n'.join(contentBlocks[1::])
    f.close()
    f = codecs.open(mmdfile,'w','utf-8')
    f.write(content)
  f.close()


def convertPelican():
  for c in currentDirList:
    tokens = c.split('-')
    year = tokens[0]
    month = tokens[1]
    day = tokens[2]
    yearDir = rootDestDir + '/' + year
    monthDir = yearDir + '/' + month
    dayDir = monthDir + '/' + day
    safeMkDir(dayDir)
    newFileName = '-'.join(tokens[3::])
    fullOriginName = originDir + '/' + c
    fullDestName = dayDir + '/' + newFileName
    print('Copying: \n' + fullOriginName + '\n    to:\n' + fullDestName)
    shutil.copy2(fullOriginName,fullDestName)
    print('Copied: ' + fullOriginName + ' to ' + fullDestName)
    convertMmdMeta(fullDestName)


def main():
  convertPelican()

if __name__ == "__main__":
  main()
