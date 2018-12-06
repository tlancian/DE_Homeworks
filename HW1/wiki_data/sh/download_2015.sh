cd ..

cd data

cat "../file_names/files_2015.txt" | xargs -I % wget %