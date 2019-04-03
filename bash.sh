#!/bin/bash
for i in $(seq 0.1 0.1 1)
do 
python eval.py --logtostderr --pipeline_config_path=training/faster_rcnn_inception_v2_coco1.config --checkpoint_dir=training/Train_27_3 --threshold=${i}  --eval_dir=training/eval_27_3; 
echo "Welcome ${i} times"; 
done

