package main

import (
	"fmt"
	"go-algo/stripe"
	"reflect"
)

func main() {
	/*
	parse_accept_language("en", ["en-US", "fr-CA", "fr-FR"])
	returns: ["en-US"]

	parse_accept_language("fr", ["en-US", "fr-CA", "fr-FR"])
	returns: ["fr-CA", "fr-FR"]

	parse_accept_language("fr-FR, fr", ["en-US", "fr-CA", "fr-FR"])
	returns: ["fr-FR", "fr-CA"]
	 */

	// r1 := stripe.ParseAcceptLanguage("en", []string{"en-US", "fr-CA", "fr-FR"})
	// r2 := stripe.ParseAcceptLanguage("fr", []string{"en-US", "fr-CA", "fr-FR"})
	 r3 := stripe.ParseAcceptLanguage("fr-FR, fr, en", []string{"en-US", "fr-CA", "fr-FR", "en-CA"})
	// r4 := stripe.ParseAcceptLanguage("", []string{"en-US", "fr-CA", "fr-FR"})
	// r5 := stripe.ParseAcceptLanguage("en-", []string{"en-US", "fr-CA", "fr-FR"})

	/*if reflect.DeepEqual(r1, []string{"en-US"}) {
		fmt.Println(r1, true)
	} else {
		fmt.Println(r2, false)
	}

	if reflect.DeepEqual(r2, []string{"fr-CA", "fr-FR"}) {
		fmt.Println(r2, true)
	} else {
		fmt.Println(r2, false)
	}*/


	if reflect.DeepEqual(r3, []string{"fr-FR", "fr-CA"}) {
		fmt.Println(r3, true)
	} else {
		fmt.Println(r3, false)
	}

	/*
	if reflect.DeepEqual(r4, []string{}) {
		fmt.Println(r4, true)
	} else {
		fmt.Println(r4, false)
	}

	if reflect.DeepEqual(r5, []string{}) {
		fmt.Println(r5, true)
	} else {
		fmt.Println(r5, false)
	}*/
}
