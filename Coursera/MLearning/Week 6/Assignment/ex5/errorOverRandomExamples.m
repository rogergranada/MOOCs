function errorOverRandomExamples(X_poly, y, X_poly_val, yval, X, mu, sigma, p)
    % Randomly separates training and validation sets multiple times and generate the
    % error for each iteration. The final errors are computed as the mean of the generated
    % errors.

    lambda = 0.01;
    rand_iter = 50;

    Xy_poly      = [X_poly y];
    Xy_poly_val  = [X_poly_val yval];
    m_poly       = size (Xy_poly, 1);  % /2

    error_train_rand = zeros(3, m_poly); % every row is a vector containing the errors for each training set size
    error_val_rand   = zeros(3, m_poly);

    for i = 1:rand_iter
      % get 12 random training set examples
      Xy_poly_rand    = Xy_poly(randperm (size (Xy_poly, 1)), :)(1:m_poly, :);
      X_poly_rand     = Xy_poly_rand(:, 1:(size(Xy_poly_rand, 2) - 1));
      y_rand          = Xy_poly_rand(:, size(Xy_poly_rand, 2));

      % get 12 random cross validation examples
      Xy_poly_val_rand = Xy_poly_val(randperm (size (Xy_poly_val, 1)), :)(1:size (Xy_poly_val, 1), :);
      X_poly_val_rand  = Xy_poly_val_rand(:, 1:(size(Xy_poly_val_rand, 2) - 1));
      yval_rand        = Xy_poly_val_rand(:, size(Xy_poly_val_rand, 2));

      [theta] = trainLinearReg(X_poly_rand, y_rand, lambda);

      [et, ev] = learningCurve(X_poly_rand, y_rand, X_poly_val_rand, yval_rand, lambda);
      error_train_rand(i, :) = et';
      error_val_rand(i, :)   = ev';
    end

    error_train = mean(error_train_rand, 1)';
    error_val   = mean(error_val_rand, 1)';


    % Plot training data and fit
    figure(1);
    plot(X, y, 'rx', 'MarkerSize', 10, 'LineWidth', 1.5);
    plotFit(min(X), max(X), mu, sigma, theta, p);
    xlabel('Change in water level (x)');
    ylabel('Water flowing out of the dam (y)');
    title (sprintf('Polynomial Regression Fit (lambda = %f)', lambda));

    figure(2);
    plot(1:m_poly, error_train, 1:m_poly, error_val);

    title(sprintf('Polynomial Regression Learning Curve (lambda = %f, rand_iter= %f', lambda, rand_iter));
    xlabel('Number of training examples')
    ylabel('Error')
    axis([0 13 0 100])
    legend('Train', 'Cross Validation')

    fprintf('Polynomial Regression (lambda = %f)\n\n', lambda);
    fprintf('# Training Examples\tTrain Error\tCross Validation Error\n');
    for i = 1:m_poly
        fprintf('  \t%d\t\t%f\t%f\n', i, error_train(i), error_val(i));
    end
end
