#!/bin/python3

import glob
import tqdm
import os
import subprocess
import lxml.etree as ET
from typing import Iterable, Optional
# java -jar LineSegmentationEvaluator.jar -igt ../gt/microfilms/245v-246r.jpg -xgt ../gt/microfilms/245v-246r.xml -xp ../prediction/segmentation/245v-246r.lines.page.xml -csv

do_kraken = True 
do_compare = False


xsl = ET.XSLT(ET.parse("./data-wrangling/segmentation-xml-simplification.xsl"))

def xsl_run(files: Iterable[str], suffix: Optional[str] = None):
    """ Applies XSLT at [XSL_PATH] on [FILES]"""
    for file_path in tqdm.tqdm(files):
        xml = ET.parse(file_path)
        new_xml = xsl(xml)
        new_file = file_path
        if suffix:
            new_file = new_file.replace(".xml", suffix)
        with open(new_file, "w") as out:
            out.write(str(new_xml))


for file in tqdm.tqdm(glob.glob("./gt/microfilms/**/*.jpg")):
	image = "/".join(file.split("/")[-2:])
	xml = ".".join(image.split(".")[:-1])

	os.makedirs(os.path.dirname(f"./prediction/segmentation/{image}"), exist_ok=True)

	if do_kraken:
		proc_output = subprocess.call(
			f"kraken --raise-on-error -x -i ./gt/microfilms/{image} ./prediction/segmentation/{xml}.region.xml segment --model ./models/segmentation/Regions_Complx_2_39.mlmodel".split()
		)
		proc_output = subprocess.call(
			f"kraken --raise-on-error -x -i ./prediction/colorization/{image} ./prediction/segmentation/{xml}.colors.region.xml segment --model ./models/segmentation/Regions_Complx_2_39.mlmodel".split()
		)
		# If do kraken, apply xsl as well
		# xsl_run([f"./prediction/segmentation/{xml}.lines.xml", f"./prediction/segmentation/{xml}.colors.lines.xml", f"./gt/microfilms/{xml}.xml"])
