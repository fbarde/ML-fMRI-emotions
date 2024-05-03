% Make plot in latex style
set(groot, 'defaultAxesTickLabelInterpreter','latex');
set(groot, 'defaultLegendInterpreter','latex');
set(groot, 'defaultTextInterpreter', 'latex');
set(groot, 'defaultAxesFontSize', 10);
set(groot, 'defaultLineLinewidth', 1);
format long;

x_axis = [1, 2 , 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13];
% Random forest 
precision_random_forest = [0.41, 0.38, 0.32, 0.56, 0.32, 0.23, 0.41, 0.66, 0.21, 0.12, 0.32, 0.21, 0.44];

% Decision Tree classifier
precision_dec_tree = [0, 0.72, 0.34, 0.18, 0, 0, 0, 0, 0.22, 0.15, 0.29, 0, 0.29];
    
%SVM 
precision_SVM = [0.27, 0.35, 0.27, 0.2, 0.12, 0.26, 0.31, 0.33, 0.24, 0.08, 0.35, 0.4, 0.21];

%KNN
precision_KNN = [0, 0.29, 0.33, 0.2, 0, 0, 0, 0, 0.28, 0.44, 0.27, 0, 0];

%Log Regression
precision_log_reg = [0.18, 0.32, 0.26, 0.27, 0.09, 0.16, 0.26, 0.29, 0.31, 0.07, 0.37, 0.25, 0.22];

% Convolutional NN
precision_CNN = [0.17, 0.38, 0.17, 0.17, 0.10, 0.16, 0.29, 0.23, 0.18, 0.16, 0.35, 0.12, 0.3];

% Fully connected NN
precision_FCNN = [0,0,0,0,0,0,0,0,0,0,0.26,0,0];

% Order everything alphabetically 

% Switch Anxiety and Sad
precision_random_forest([2 5]) = precision_random_forest([5 2]);
precision_dec_tree([2 5]) = precision_dec_tree([5 2]);
precision_SVM([2 5]) = precision_SVM([5 2]);
precision_KNN([2 5]) = precision_KNN([5 2]);
precision_log_reg([2 5]) = precision_log_reg([5 2]);
precision_CNN([2 5]) = precision_CNN([5 2]);
precision_FCNN([2 5]) = precision_FCNN([5 2]);

% Switch Shame and Contempt
precision_random_forest([3 8]) = precision_random_forest([8 3]);
precision_dec_tree([3 8]) = precision_dec_tree([8 3]);
precision_SVM([3 8]) = precision_SVM([8 3]);
precision_KNN([3 8]) = precision_KNN([8 3]);
precision_log_reg([3 8]) = precision_log_reg([8 3]);
precision_CNN([3 8]) = precision_CNN([8 3]);
precision_FCNN([3 8]) = precision_FCNN([8 3]);

% Switch Fear and Sad
precision_random_forest([5 6]) = precision_random_forest([6 5]);
precision_dec_tree([5 6]) = precision_dec_tree([6 5]);
precision_SVM([5 6]) = precision_SVM([6 5]);
precision_KNN([5 6]) = precision_KNN([6 5]);
precision_log_reg([5 6]) = precision_log_reg([6 5]);
precision_CNN([5 6]) = precision_CNN([6 5]);
precision_FCNN([5 6]) = precision_FCNN([6 5]);

% Switch Happiness and Sad
precision_random_forest([6 11]) = precision_random_forest([6 11]);
precision_dec_tree([6 11]) = precision_dec_tree([6 11]);
precision_SVM([6 11]) = precision_SVM([6 11]);
precision_KNN([6 11]) = precision_KNN([6 11]);
precision_log_reg([6 11]) = precision_log_reg([6 11]);
precision_CNN([6 11]) = precision_FCNN([6 11]);

% Switch Surprise and Love
precision_random_forest([7 12]) = precision_random_forest([12 7]);
precision_dec_tree([7 12]) = precision_dec_tree([12 7]);
precision_SVM([7 12]) = precision_SVM([12 7]);
precision_KNN([7 12]) = precision_KNN([12 7]);
precision_log_reg([7 12]) = precision_log_reg([12 7]);
precision_CNN([7 12]) = precision_FCNN([12 7]);

% Switch Sad and Shame
precision_random_forest([8 11]) = precision_random_forest([11 8]);
precision_dec_tree([8 11]) = precision_dec_tree([11 8]);
precision_SVM([8 11]) = precision_SVM([11 8]);
precision_KNN([8 11]) = precision_KNN([11 8]);
precision_log_reg([8 11]) = precision_log_reg([11 8]);
precision_CNN([8 11]) = precision_FCNN([11 8]);

% Switch Warhearth and Shame
precision_random_forest([10 11]) = precision_random_forest([11 10]);
precision_dec_tree([10 11]) = precision_dec_tree([11 10]);
precision_SVM([10 11]) = precision_SVM([11 10]);
precision_KNN([10 11]) = precision_KNN([11 10]);
precision_log_reg([10 11]) = precision_log_reg([11 10]);
precision_CNN([10 11]) = precision_FCNN([11 10]);

% Switch Warhearth and Surprise
precision_random_forest([11 12]) = precision_random_forest([11 12]);
precision_dec_tree([11 12]) = precision_dec_tree([11 12]);
precision_SVM([11 12]) = precision_SVM([11 12]);
precision_KNN([11 12]) = precision_KNN([11 12]);
precision_log_reg([11 12]) = precision_log_reg([11 12]);
precision_CNN([11 12]) = precision_FCNN([11 12]);

scatter(x_axis, precision_random_forest, '<')
hold on
scatter(x_axis, precision_dec_tree, 'o')
scatter(x_axis, precision_SVM, '*')
scatter(x_axis, precision_KNN, 'x')
scatter(x_axis, precision_log_reg, '+')
scatter(x_axis, precision_CNN, 's')
scatter(x_axis, precision_FCNN,'d')

%Plot results
xticks ([1, 2 ,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
xticklabels({'Anger', 'Anxiety','Contempt' , 'Disgust','Fear' , 'Happiness','Love' ,'Sad' , 'Satisfaction', 'Shame', 'Surprise', 'WarmHeart' , 'Neutral'})
xtickangle(45)
xlabel('Emotion')
ylabel('Precision')
legend('Random Forest', 'Decision Tree', 'SVM', 'KNN', 'Logistic Regression', 'CNN', 'FCNN')

