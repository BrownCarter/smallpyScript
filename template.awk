#/bin/env awk -f
BEGIN {
  template="letter1.txt"
  NR=0
  getline
  output="final"
}

{
  firstname=$1
  lastname=$2
  position=$3

  outfile=(output NR ".txt")

  while((getline ln < template) > 0){
    sub(/{firstname}/, firstname, ln)
    sub(/{lastname}/, lastname, ln)
    sub(/{position}/, position, ln)
    print(ln)
  }
  close(outfile)
  close(template)
}

