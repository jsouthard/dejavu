package main

import (
	"log"

	"github.com/docopt/docopt-go"
)

func main() {
	usage := `	
Usage:
	program <req> [--option=ARG]
	program -h | --help

Options:
	req           Required argument
	--option=ARG  Optional argument [default: foo]
	-h --help     Show this screen.
`

	args, err := docopt.Parse(usage, nil, true, "", false)
	if err != nil {
		log.Fatalf("Error Parsing Options: %v", err)
	}

	// Implementation

}
