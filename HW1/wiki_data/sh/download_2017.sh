cd ..

cd data

cat "../file_names/files_2017.txt" | xargs -I % wget %