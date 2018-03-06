#!/usr/bin/env python

from glob import glob
import os
from os.path import basename, join
from pyidr.file_pattern import FilePattern

TIMEPOINTS = 40

base = "/uod/idr/filesets/idr0041-cai-mitoticatlas/"
plates = "idr-metadata/idr0041-cai-mitoticatlas/patterns/"

assays = [join(base, x) for x in os.listdir(base)]
assays = filter(os.path.isdir, assays)
for assay in assays:
    cells = [x for x in glob(assay + "/*") if not x.endswith("Calibration")]
    if not cells:
        print "Empty directory: %s" % assay
        continue
    for cell in cells:
        rawtifs = sorted([x for x in glob(cell + "/rawtif/*")
            if not x.endswith("Thumbs.db")])
        assert len(rawtifs) == TIMEPOINTS, (
            "Incorrect number of files on %s" % cell)
        pattern = join(cell, "rawtif",
            basename(rawtifs[0])[:-6] + "<01-%g>" % TIMEPOINTS + ".tif")

        assert list(FilePattern(pattern).filenames()) == rawtifs
