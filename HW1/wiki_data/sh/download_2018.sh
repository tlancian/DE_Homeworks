cd ..

cd data

cat "../file_names/files_2018.txt" | xargs -I % wget %