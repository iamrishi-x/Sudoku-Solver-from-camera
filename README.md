# Sudoku-Solver-from-camera
Sudoku solving using camera which uses python,opencv,keras,tensorflow for digit recognition and backtracking .

Note : make sure you have installed python3,keras,tensorflow,opencv.

Files Contain ...

1.Main_TestWebcam.py [ main file to run ] 
  
  purpose :
  
          1.This file is use to get answer from sudoku image capture through the webcam
          first it detect the sudoku grid and when it shows 'Detected :)' symbol Press
          'C' to capture .
          
          2.After capturing it process the image and detect no written on grid for this
          it uses pretrained model from model folder 'model/digit_recognisor.h5' present
          at project directory .
          
          3.After that it uses backtraking algorithm to predict grid from 'sudoku_Algorithm.py'
          file .
          
2.sudoku_Algorithm.py

  purpose : 
  
          1.Contain main algorithm
          Just used for temporary purpose after it i have to switch it to AI for
          sudoku solvingFile    : 
        
        
Folders Contain ...

1.model

    Contains pretrained model 'model/digit_recognisor.h5'
  
2.images

    Use image to show to camera when code runs, Use ur smartphone to show sudoku image.
 
