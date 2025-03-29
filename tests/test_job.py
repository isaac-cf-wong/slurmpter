from __future__ import annotations

import tempfile

from slurmpter import SlurmJob

expected_TestSlurmJob_test_build_output = """#!/bin/bash
#SBATCH --job-name=test_slurmjob_build
#SBATCH --output=slurm/output/test_slurmjob_build.output
#SBATCH --error=slurm/error/test_slurmjob_build.error
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --sbatch_option_0=sbatch_xoption_0
#SBATCH --sbatch_option_1=sbatch_xoption_1

extra_line_0
extra_line_1

module load module_0
module load module_1

srun --srun_option_0=srun_xoption_0 --srun_option_1=srun_xoption_1 executable --arg arg_0 &
srun --srun_option_0=srun_xoption_0 --srun_option_1=srun_xoption_1 executable --arg arg_1 &
srun --srun_option_0=srun_xoption_0 --srun_option_1=srun_xoption_1 executable --arg arg_2 &
srun --srun_option_0=srun_xoption_0 --srun_option_1=srun_xoption_1 executable --arg arg_3 &
srun --srun_option_0=srun_xoption_0 --srun_option_1=srun_xoption_1 executable --arg arg_4 &
wait
"""

expected_job_str = "SlurmJob(name=test_str, executable=test_exec, "\
                   "_slurm_extra_srun_options=['ntasks=1', 'exclusive'],"\
                   " error=slurm/error, output=slurm/output, submit=slurm/submit)"


def test_build():
    with tempfile.TemporaryDirectory() as temp_dir:
        error = f"{temp_dir}/error"
        output = f"{temp_dir}/output"
        submit = f"{temp_dir}/submit"

        job = SlurmJob(name="test_slurmjob_build",
                        executable="executable",
                        submit=submit,
                        output=output,
                        error=error,
                        nodes=1,
                        ntasks_per_node=1,
                        cpus_per_task=4,
                        mem_per_node="16G",
                        extra_sbatch_options=["sbatch_option_0=sbatch_xoption_0",
                                                "sbatch_option_1=sbatch_xoption_1"],
                        extra_srun_options=["srun_option_0=srun_xoption_0",
                                            "srun_option_1=srun_xoption_1"],
                        extra_lines=["extra_line_0", "extra_line_1"],
                        modules=["module_0", "module_1"],
                        arguments=["--arg arg_0", "--arg arg_1"])
        job.add_arg("--arg arg_2")
        job.add_args(["--arg arg_3", "--arg arg_4"])
        job.build(fancyname=False)
        with open(f"{temp_dir}/submit/test_slurmjob_build.submit") as f:
            data = f.read()
        assert data == expected_TestSlurmJob_test_build_output

def test_str():
    with tempfile.TemporaryDirectory() as temp_dir:
        error = f"{temp_dir}/error"
        output = f"{temp_dir}/output"
        submit = f"{temp_dir}/submit"

        job = SlurmJob(name="test_str",
                        executable="test_exec",
                        submit=submit,
                        output=output,
                        error=error)

        assert str(job) == expected_job_str
