# Open Innovations Reference Data

This repository manages common reference data that we use across Open
Innovations. It's an experiment at the moment. We're trying out the
[`dvc`](https://dvc.org) tool which works with `git` to manage data and
pipelines.

## Using the data

To use this repository and data, you will need to
[install `dvc`](https://dvc.org/doc/install)

You can see the contents of thW repository with the
[`dvc list`](https://dvc.org/doc/command-reference/list) command:

```
dvc list --recursive --dvc-only https://github.com/open-innovations/reference-data
```

Processed reference data is held in the `output` folder. To see what's
available, use

```
dvc list --recursive --dvc-only https://github.com/open-innovations/reference-data output
```

At present, these are the files:

* `output/onspd-extract.csv`.  
  Cut-down version of the ONS Postcode Directory. Includes the following
  columns: `pcds`, `oslaua`, `osward`, `lsoa11`, `msoa11`. See [the ONS Postcode
  Directory (below)](#ONS%20Postcode%20Directory) for details.

To download a file, use the `dvc get` subcommand. NB this does not require you
to make the repository a DVC repo. It's essentially a way of provisioning a copy
of the file locally.

```
dvc get https://github.com/open-innovations/reference-data output/onspd-extract.csv
```

This will put the file into your current directory. You can either `cd` to the
directory you want to put the file into, or use the `--out` flag to specify the
output path.

### Working within a DVC repository

If you wish to retain a link to the original file you can instead use the `dvc
import` command. This allows the file to be updated if the reference changes.
You will need to be in a DVC repo for this to work. You can set this up by
running `dvc init`.

```
dvc import https://github.com/open-innovations/reference-data output/onspd-extract.csv
```

In the latter case, DVC will update your gitignore to prevent the data file
being checked in, but will add a small `<filename>.dvc` file containing
metadata. This helps ensure the data you imported is kept in sync with the
upstream source. This includes populating fresh clones of the git repo with
reference data.

To see the state of any files you might have imported, run the
[`dvc status`](https://dvc.org/doc/command-reference/status) command.

If any files are missing or changed, the files can be provisioned by running
[`dvc pull`](https://dvc.org/doc/command-reference/pull).

The file will be tied to the state of the repo when it was imported. To move
forward, you can issue the
[`dvc update`](https://dvc.org/doc/command-reference/update) command.

```
dvc update --rev main --recursive . 
```

## Datasets

### ONS Postcode Directory

This data is extracted from the
[most recent ONS Postcode Directory](https://geoportal.statistics.gov.uk/search?collection=Dataset&sort=-created&tags=all(PRD_ONSPD)).

The following fields are extrated, per the original ONSPD spec. This is
extracted from the user guide contained in the ONSPD zip file.

* `pcds`  
  _Unit postcode - variable length (e-Gif) version_  
  2, 3 or 4-character outward code; Single space; 3-character inward code
* `oslaua`   
  _Local authority district (LAD) / unitary authority (UA) / metropolitan district
  (MD) / London borough (LB) / council area (CA) / district council area (DCA)_  
  The current LAD/UA to which the postcode has been assigned. Pseudo codes are included for Channel Islands and Isle of Man. The field will otherwise be blank for postcodes with no grid reference.
* `osward`  
  _(Electoral) ward / division_  
  The current administrative / electoral area to which the postcode has been assigned. Pseudo codes are included for Channel Islands and Isle of Man. The field will otherwise be blank for postcodes with no grid reference.
* `lsoa11`  
  _2011 Census Lower Layer Super Output Area (LSOA)/ Data Zone (DZ)/ SOA_  
  The 2011 Census LSOA (England and Wales), SOA (Northern Ireland) and DZ (Scotland) code. Pseudo codes are included for Channel Islands and Isle of Man. The field will otherwise be blank for postcodes with no grid reference. N.B. NI SOAs remain unchanged from 2001.
* `msoa11`  
  _2011 Census Middle Layer Super Output Area (MSOA) / Intermediate Zone (IZ)_  
  The 2011 Census MSOA code for England and Wales and IZ zone for Scotland. Pseudo codes are included for Northern Ireland, Channel Islands and Isle of Man. The field will otherwise be blank for postcodes with no grid reference.