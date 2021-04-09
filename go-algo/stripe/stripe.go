package stripe

import (
	"fmt"
	"regexp"
	"strings"
)

// fr-FR, fr
func ParseAcceptLanguage(reqHeaders string, acceptedHeaders []string) []string {
	retList := make([]string, 0, len(acceptedHeaders))
	retMap := map[string]bool{}
	for _, ah := range acceptedHeaders {
		exactMatchRegexp := regexp.MustCompile(ah)
		matchedString := exactMatchRegexp.FindString(reqHeaders)
		if matchedString != "" && !retMap[ah] {
			retMap[ah] = true
			retList = append(retList, ah)
			continue
		}

		dashIdx := strings.Index(ah, "-")
		langMatchRegexp := regexp.MustCompile(fmt.Sprintf("(^%s)(-\\w+?)?", ah[:dashIdx]))
		fmt.Println(langMatchRegexp.FindStringSubmatch(reqHeaders))
	}

	return retList
}

func Contains(headers []string, header string) bool {
	contains := false
	for _, head := range headers {
		if head == header {
			contains = true
			break
		}
	}
	return contains
}
