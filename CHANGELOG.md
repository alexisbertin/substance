# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/) 
and this project adheres to [Semantic Versioning](http://semver.org/).

## [0.9a1] - 2017-02-01
### Added
- Official Linux 64-bit support
- Support for engine-defined project aliases
- New `substance aliases` command
- Engine can be specified on any command using `-e` now.
- Add `-i` option to `substance sync` for easy fix with unison failures.
- More detailed documentation

### Changed
- `substance switch` now restarts containers by default (disable with `--keep-containers`).

## [0.8a4] - 2017-02-01
### Fixed
- sync crash on Windows

## [0.8a3] - 2017-01-31
### Fixed
- pip install on 0.8a2 was broken.

## [0.8a2] - 2017-01-31
### Fixed
- Make sure proper `docker login` is performed on a `substance switch`.

## [0.8a1] - 2017-01-31
### Added
- Official Windows support under Cygwin-64.
- New mode of sync: unison
- Substance box upgrade to 0.6 to have unison packed in.
- `substance launch` will not automatically start containers if an active environment is set.