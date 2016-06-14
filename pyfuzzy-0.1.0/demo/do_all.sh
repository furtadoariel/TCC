export PYTHONPATH=../../pyfuzzy${PYTHONPATH:+:$PYTHONPATH}
echo $PYTHONPATH
for i in `find . -name '*.fcl' -type f -o -type l` ; do
    echo $i
    i=`basename $i`
    python FCLTest.py $i | tee $i.log
done