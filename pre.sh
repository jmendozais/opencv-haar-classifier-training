list=$1
list_dir="${list%.*}"

# make list_dir
rm -rf $list_dir
mkdir $list_dir

# copy images to list_dir
python copy_data.py train_scaled_patches $list

find ./${list_dir} -iname "*.jpg" > ${list_dir}_positives.txt
