# Your job will use 1 node, 12 cores, and 32gb of memory total.
#PBS -q standard
#PBS -l select=1:ncpus=12:mem=32gb:pcmem=6gb
### Specify a name for the job
#PBS -N star_test
### Specify the group name
#PBS -W group_list=baltrus
### Used if job requires partial node only
#PBS -l place=pack:shared
### CPUtime required in hhh:mm:ss. The maximum is 720:00:00
### Leading 0's can be omitted e.g 48:0:0 sets 48 hours
#PBS -l cput=010:00:00
### Walltime is created by cputime divided by total cores.
### This field can be overwritten by a longer time
#PBS -l walltime=01:00:00

module load star

cd $PBS_O_WORKDIR
STAR --genomeDir star_index/ --readFilesCommand gunzip -c --readFilesIn work_data/$SAMPLE\_L001_R1_001.fastq.gz,work_data/$SAMPLE\_L002_R1_001.fastq.gz work_data/$SAMPLE\_L001_R2_001.fastq.gz,work_data/$SAMPLE\_L002_R2_001.fastq.gz --runThreadN 12 --outFileNamePrefix star_aligned/$SAMPLE/$SAMPLE\_star --outSAMtype BAM Unsorted
