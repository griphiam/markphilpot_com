for i in `ls *.md`
do
	echo -e "---\n$(cat $i)" > $i
	sed -i 's/^Title:/title:/' $i
	sed -i 's/^Date:/date:/' $i
	sed -i 's/^Tags:(.*)/tags: [\1]/' $i
	sed -i 's/^Category:/category:/' $i
	sed -i 's/^Slug:/slug:/' $i
	sed -i 's/^$/---\n\n/' $i
done