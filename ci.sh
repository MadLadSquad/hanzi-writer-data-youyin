#!/usr/bin/env bash

merge_data()
{
	rm "$1"/all.json || exit
	for file in "$1"/*.json; do
		n="${#1}"
		tmp="${file:$n}"
		tmp="${tmp%.json}"
		if [ -n "$(ls -A ../hanzi-writer-data-zh/data/"${tmp}".json 2>/dev/null)" ] && [ "$2" != "0" ]; then
			if [ ! -n "$(ls -A ../hanzi-writer-data-zh/data/"${tmp}"-"$2".json 2>/dev/null)" ]; then
				cp "$1"/"${tmp}".json ../hanzi-writer-data-zh/data/"${tmp}"-"$2".json || exit
			fi
		else
			cp "$1"/"${tmp}".json ../hanzi-writer-data-zh/data/ || exit
		fi
	done
}

init()
{
	cd ThirdParty/hanzi-writer-data-zh || exit
	python3 stroke_data_parser.py || exit
	rm data/all.json || exit
	cp data/*.json ../../data/ || exit

	# Generate Japanese data first, so that we can merge things well
	cd ../hanzi-writer-data-jp || exit
	patch stroke_data_parser.py ../../stroke-parser.patch || exit

	mkdir data-ko data-kana data-hz data-hz-t || exit
	python3 stroke_data_parser.py JaKana data-kana 0 || exit
	python3 stroke_data_parser.py Ja data 1 || exit
	python3 stroke_data_parser.py Ko data-ko 1 || exit

	merge_data data/ jp
	merge_data data-ko/ ko
	merge_data data-kana/ 0

	cd ../hanzi-writer-data-zh/ || exit
	cp data/*.json ../../data/ || exit
}

init
