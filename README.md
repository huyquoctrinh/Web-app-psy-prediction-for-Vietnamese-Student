**[This code implement and develop from CNN for Text Classification in Tensorflow & Classify text with Bert Tensorflow" blog post.](http://www.wildml.com/2015/12/implementing-a-cnn-for-text-classification-in-tensorflow/)**(https://www.tensorflow.org/tutorials/text/classify_text_with_bert)

It is slightly simplified implementation of Kim's [Convolutional Neural Networks for Sentence Classification](http://arxiv.org/abs/1408.5882) paper in Tensorflow.

## Requirements

- Python 3
- Tensorflow==2.4.1
- Numpy
- Flask
## Training
With CNN train.py
With Bert classify_text_with_bert.ipynb
## Evaluating
Download model from
```bash
./eval.py --eval_train --checkpoint_dir="./runs/1459637919/checkpoints/"
```

Replace the checkpoint dir with the output from the training. To use your own data, change the `eval.py` script to load your data.

## Run Server
API: sudo python3 bert_sv.py
WEB U.I: npm start
## References

- [Convolutional Neural Networks for Sentence Classification](http://arxiv.org/abs/1408.5882)
- [A Sensitivity Analysis of (and Practitioners' Guide to) Convolutional Neural Networks for Sentence Classification](http://arxiv.org/abs/1510.03820)
