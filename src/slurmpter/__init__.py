from __future__ import annotations

from pycondor.dagman import Dagman
from pycondor.job import Job as DagmanJob

from .job import SlurmJob
from .slurm import Slurm

__version__ = "1.0.1"

__all__ = [
    'DagmanJob',
    'Dagman',
    'Slurm',
    'SlurmJob'
]
