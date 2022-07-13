package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main(){
  //box := []int{1, 2, 6, 8}
  data, err := os.Open("./employee1.tsv")
  if err != nil{
    panic(err)
  }
  scan := bufio.NewScanner(data)
  scan.Split(bufio.ScanLines)
  for scan.Scan() {
    word := scan.Text()
    block := strings.Fields(word)
    first_name := block[0]
    last_name := block[1]
    position := block[2]
    letter, ex := os.ReadFile("./letter1.txt")
    if ex != nil {
      panic(ex)
    }

    letter1 := string(letter)
    letter1 = strings.Replace(letter1, "{firstname}", first_name, -1)
    letter1 = strings.Replace(letter1, "{lastname}", last_name, -1)
    letter1 = strings.Replace(letter1, "{position}", position, -1)
    fmt.Println(letter1) 
  }
  data.Close()
}

