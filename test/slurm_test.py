import unittest

from slurmpter import SlurmJob, Slurm

expected_TestSlurm_test_build_slurm_output = """#!/bin/bash
#SBATCH --job-name=test_slurm_build_slurm
#SBATCH --output=slurm/submit/test_slurm_build_slurm.output
#SBATCH --error=slurm/submit/test_slurm_build_slurm.error

extra_line_0
extra_line_1

jid0=($(sbatch slurm/submit/test_slurm_build_job_0.submit))
jid1=($(sbatch --dependency=afterok:${jid0[-1]} slurm/submit/test_slurm_build_job_1.submit))
jid2=($(sbatch --dependency=afterok:${jid0[-1]}:${jid1[-1]} slurm/submit/test_slurm_build_job_2.submit))
jid3=($(sbatch --dependency=afterok:${jid1[-1]}:${jid2[-1]} slurm/submit/test_slurm_build_job_3.submit))
jid4=($(sbatch --dependency=afterok:${jid2[-1]} slurm/submit/test_slurm_build_job_4.submit))
"""

expected_TestSlurm_test_build_job_0_output = """#!/bin/bash
#SBATCH --job-name=test_slurm_build_job_0
#SBATCH --output=slurm/output/test_slurm_build_job_0.output
#SBATCH --error=slurm/error/test_slurm_build_job_0.error
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

srun --srun_option_0=srun_xoption_0 --srun_option_1=srun_xoption_1 executable_0 --arg arg_0 &
srun --srun_option_0=srun_xoption_0 --srun_option_1=srun_xoption_1 executable_0 --arg arg_1 &
srun --srun_option_0=srun_xoption_0 --srun_option_1=srun_xoption_1 executable_0 --arg arg_2 &
srun --srun_option_0=srun_xoption_0 --srun_option_1=srun_xoption_1 executable_0 --arg arg_3 &
srun --srun_option_0=srun_xoption_0 --srun_option_1=srun_xoption_1 executable_0 --arg arg_4 &
wait
"""
expected_TestSlurm_test_build_job_1_output = """#!/bin/bash
#SBATCH --job-name=test_slurm_build_job_1
#SBATCH --output=slurm/output/test_slurm_build_job_1.output
#SBATCH --error=slurm/error/test_slurm_build_job_1.error
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

srun --srun_option_0=srun_xoption_0 --srun_option_1=srun_xoption_1 executable_1 --arg arg_0 &
srun --srun_option_0=srun_xoption_0 --srun_option_1=srun_xoption_1 executable_1 --arg arg_1 &
srun --srun_option_0=srun_xoption_0 --srun_option_1=srun_xoption_1 executable_1 --arg arg_2 &
srun --srun_option_0=srun_xoption_0 --srun_option_1=srun_xoption_1 executable_1 --arg arg_3 &
srun --srun_option_0=srun_xoption_0 --srun_option_1=srun_xoption_1 executable_1 --arg arg_4 &
wait
"""

expected_TestSlurm_test_build_job_2_output = """#!/bin/bash
#SBATCH --job-name=test_slurm_build_job_2
#SBATCH --output=slurm/output/test_slurm_build_job_2.output
#SBATCH --error=slurm/error/test_slurm_build_job_2.error
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

srun --srun_option_0=srun_xoption_0 --srun_option_1=srun_xoption_1 executable_2 --arg arg_0 &
srun --srun_option_0=srun_xoption_0 --srun_option_1=srun_xoption_1 executable_2 --arg arg_1 &
srun --srun_option_0=srun_xoption_0 --srun_option_1=srun_xoption_1 executable_2 --arg arg_2 &
srun --srun_option_0=srun_xoption_0 --srun_option_1=srun_xoption_1 executable_2 --arg arg_3 &
srun --srun_option_0=srun_xoption_0 --srun_option_1=srun_xoption_1 executable_2 --arg arg_4 &
wait
"""

expected_TestSlurm_test_build_job_3_output = """#!/bin/bash
#SBATCH --job-name=test_slurm_build_job_3
#SBATCH --output=slurm/output/test_slurm_build_job_3.output
#SBATCH --error=slurm/error/test_slurm_build_job_3.error
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

srun --srun_option_0=srun_xoption_0 --srun_option_1=srun_xoption_1 executable_3 --arg arg_0 &
srun --srun_option_0=srun_xoption_0 --srun_option_1=srun_xoption_1 executable_3 --arg arg_1 &
srun --srun_option_0=srun_xoption_0 --srun_option_1=srun_xoption_1 executable_3 --arg arg_2 &
srun --srun_option_0=srun_xoption_0 --srun_option_1=srun_xoption_1 executable_3 --arg arg_3 &
srun --srun_option_0=srun_xoption_0 --srun_option_1=srun_xoption_1 executable_3 --arg arg_4 &
wait
"""

expected_TestSlurm_test_build_job_4_output = """#!/bin/bash
#SBATCH --job-name=test_slurm_build_job_4
#SBATCH --output=slurm/output/test_slurm_build_job_4.output
#SBATCH --error=slurm/error/test_slurm_build_job_4.error
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

srun --srun_option_0=srun_xoption_0 --srun_option_1=srun_xoption_1 executable_4 --arg arg_0 &
srun --srun_option_0=srun_xoption_0 --srun_option_1=srun_xoption_1 executable_4 --arg arg_1 &
srun --srun_option_0=srun_xoption_0 --srun_option_1=srun_xoption_1 executable_4 --arg arg_2 &
srun --srun_option_0=srun_xoption_0 --srun_option_1=srun_xoption_1 executable_4 --arg arg_3 &
srun --srun_option_0=srun_xoption_0 --srun_option_1=srun_xoption_1 executable_4 --arg arg_4 &
wait
"""

expected_slurm_str = "Slurm(name=test_slurm_build_slurm, n_nodes=5, _built=True, "\
                     "error_file=slurm/submit/test_slurm_build_slurm.error, extra_lines=['"\
                     "extra_line_0', 'extra_line_1'], output_file=slurm/submit/test_slurm_"\
                     "build_slurm.output, submit=slurm/submit, submit_file=slurm/submit/"\
                     "test_slurm_build_slurm.submit, submit_name=test_slurm_build_slurm)"


class TestSlurm(unittest.TestCase):

    def test_build(self):
        error = "slurm/error"
        output = "slurm/output"
        submit = "slurm/submit"

        slurm = Slurm(name="test_slurm_build_slurm",
                      submit=submit,
                      extra_lines=["extra_line_0", "extra_line_1"])

        job_0 = SlurmJob(name="test_slurm_build_job_0",
                         executable="executable_0",
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
        slurm.add_job(job_0)
        job_0.add_arg("--arg arg_2")
        job_0.add_args(["--arg arg_3", "--arg arg_4"])

        job_1 = SlurmJob(name="test_slurm_build_job_1",
                         executable="executable_1",
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
                         arguments=["--arg arg_0", "--arg arg_1"],
                         slurm=slurm)
        job_1.add_parent(job_0)
        job_1.add_arg("--arg arg_2")
        job_1.add_args(["--arg arg_3", "--arg arg_4"])

        job_2 = SlurmJob(name="test_slurm_build_job_2",
                         executable="executable_2",
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
                         arguments=["--arg arg_0", "--arg arg_1"],
                         slurm=slurm)
        job_2.add_parents([job_0, job_1])
        job_2.add_arg("--arg arg_2")
        job_2.add_args(["--arg arg_3", "--arg arg_4"])

        job_3 = SlurmJob(name="test_slurm_build_job_3",
                         executable="executable_3",
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
                         arguments=["--arg arg_0", "--arg arg_1"],
                         slurm=slurm)
        job_3.add_arg("--arg arg_2")
        job_3.add_args(["--arg arg_3", "--arg arg_4"])

        job_4 = SlurmJob(name="test_slurm_build_job_4",
                         executable="executable_4",
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
                         arguments=["--arg arg_0", "--arg arg_1"],
                         slurm=slurm)
        job_4.add_arg("--arg arg_2")
        job_4.add_args(["--arg arg_3", "--arg arg_4"])

        job_1.add_child(job_3)
        job_2.add_children([job_3, job_4])

        slurm.build(fancyname=False)

        with open("slurm/submit/test_slurm_build_slurm.submit", "r") as f:
            data = f.read()
        self.assertEqual(data, expected_TestSlurm_test_build_slurm_output)

        with open("slurm/submit/test_slurm_build_job_0.submit", "r") as f:
            data = f.read()
        self.assertEqual(data, expected_TestSlurm_test_build_job_0_output)

        with open("slurm/submit/test_slurm_build_job_1.submit", "r") as f:
            data = f.read()
        self.assertEqual(data, expected_TestSlurm_test_build_job_1_output)

        with open("slurm/submit/test_slurm_build_job_2.submit", "r") as f:
            data = f.read()
        self.assertEqual(data, expected_TestSlurm_test_build_job_2_output)

        with open("slurm/submit/test_slurm_build_job_3.submit", "r") as f:
            data = f.read()
        self.assertEqual(data, expected_TestSlurm_test_build_job_3_output)

        with open("slurm/submit/test_slurm_build_job_4.submit", "r") as f:
            data = f.read()
        self.assertEqual(data, expected_TestSlurm_test_build_job_4_output)

        self.assertEqual(job_0.haschildren(), True)
        self.assertEqual(job_0.hasparents(), False)
        self.assertEqual(job_1.haschildren(), True)
        self.assertEqual(job_1.hasparents(), True)
        self.assertEqual(job_2.haschildren(), True)
        self.assertEqual(job_2.hasparents(), True)
        self.assertEqual(job_3.haschildren(), False)
        self.assertEqual(job_3.hasparents(), True)
        self.assertEqual(job_4.haschildren(), False)
        self.assertEqual(job_4.hasparents(), True)

        slurm.visualize("workflow.pdf")

        self.assertEqual(str(slurm), expected_slurm_str)

    def test_exception(self):
        slurm = Slurm(name="test")
        slurm_1 = Slurm(name="test_1")
        slurm_2 = Slurm(name="test_2")

        # Test forbidden function calls.
        self.assertRaises(NotImplementedError, slurm.add_child, slurm_1)
        self.assertRaises(NotImplementedError, slurm.add_children, [slurm_1, slurm_2])
        self.assertRaises(NotImplementedError, slurm.add_parent, slurm_1)
        self.assertRaises(NotImplementedError, slurm.add_parents, [slurm_1, slurm_2])
        self.assertRaises(NotImplementedError, slurm.add_subdag, slurm_1)
        self.assertRaises(NotImplementedError, slurm.haschildren)
        self.assertRaises(NotImplementedError, slurm.hasparents)
        self.assertRaises(NotImplementedError, slurm.submit_dag)
