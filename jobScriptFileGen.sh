#!bin/base
#
#SBATCH --job-name=fileGenerator
#SBATCH --output=result.txt
#
#SBATCH --ntasks=1
#SBATCH --time=10:00
#SBATCH --mem-per-cpu=1000

srun horizontalGen.py