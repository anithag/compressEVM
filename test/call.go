package main

import "fmt"
import "os/exec"

func main() {
    bytecode:=  "00\n12"
    cmd := exec.Command("python",  "gointerface.py", "-b", bytecode)
    fmt.Println(cmd.Args)
    out, err := cmd.CombinedOutput()
    if err != nil { fmt.Println(err); }
    fmt.Println(string(out))
}
