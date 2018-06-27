function [C, sigma] = dataset3Params(X, y, Xval, yval)
%EX6PARAMS returns your choice of C and sigma for Part 3 of the exercise
%where you select the optimal (C, sigma) learning parameters to use for SVM
%with RBF kernel
%   [C, sigma] = EX6PARAMS(X, y, Xval, yval) returns your choice of C and 
%   sigma. You should complete this function to return the optimal C and 
%   sigma based on a cross-validation set.
%

% You need to return the following variables correctly.
C = 1;
sigma = 0.3;

% ====================== YOUR CODE HERE ======================
% Instructions: Fill in this function to return the optimal C and sigma
%               learning parameters found using the cross validation set.
%               You can use svmPredict to predict the labels on the cross
%               validation set. For example, 
%                   predictions = svmPredict(model, Xval);
%               will return the predictions on the cross validation set.
%
%  Note: You can compute the prediction error using 
%        mean(double(predictions ~= yval))
%
values = [0.01 0.03 0.1 0.3 1 3 10 30];
min_error = inf;

fprintf('Searching for the best [C, sigma] values\n');

for C = values
    for sigma = values
        fprintf('Testing C = %f and sigma = %f', C, sigma);
        model = svmTrain(X, y, C, @(x1, x2) gaussianKernel(x1, x2, sigma));
        actual_error = mean(double(svmPredict(model, Xval) ~= yval));
        if (actual_error <= min_error)
            C_best = C;
            sigma_best = sigma;
            min_error = actual_error;
            fprintf('New best [C, sigma] = [%f %f]\n', C_best, sigma_best);
        end
    end
end
C = C_best;
sigma = sigma_best;
fprintf('Best [C, sigma] = [%f %f] with prediction error = %f\n', C, sigma, min_error);

% =========================================================================

end
