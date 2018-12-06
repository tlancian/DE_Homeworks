cd ..

cd data

cat "../file_names/files_2016.txt" | xargs -I % wget %