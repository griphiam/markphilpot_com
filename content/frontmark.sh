for i in `find . -name "*.md" | grep -v "micro"`
do
	echo "---\n$(cat $i)" > $i
	LC_CTYPE=C sed -i '' 's/^Title:[ ]*\(.*\)/title: "\1"/' $i
	LC_CTYPE=C sed -i '' 's/^Date:[ ]*\(.*\)/date: "\1\"/' $i
	LC_CTYPE=C sed -i '' 's/^Tags:[ ]*\(.*\)/tags: [\1]/' $i
	LC_CTYPE=C sed -i '' 's/^Category:/category:/' $i
	LC_CTYPE=C sed -i '' 's/^Slug:/slug:/' $i
	LC_CTYPE=C sed -i '' 's/^Summary:/summary:/' $i
	LC_CTYPE=C sed -i '' 's/^Hero: \(.*\)/Hero: "\1"/' $i
	LC_CTYPE=C sed -i '' '1,/^$/ s/^$/---\
	/' $i
done