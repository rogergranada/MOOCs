function [theta, J_history] = gradientDescent(X, y, theta, alpha, num_iters)
    %GRADIENTDESCENT Performs gradient descent to learn theta
    %   theta = GRADIENTDESENT(X, y, theta, alpha, num_iters) updates theta by 
    %   taking num_iters gradient steps with learning rate alpha

    % Initialize some useful values
    m = length(y); % number of training examples
    J_history = zeros(num_iters, 1);

    for iter = 1:num_iters
        predictions = X * theta;       % predictions of hypothesis on all m examples
        errors = (predictions - y);    %errors
        delta = 1/(m) * X' * errors;
        theta = theta - alpha * delta;

        % Save the cost J in every iteration    
        J_history(iter) = computeCost(X, y, theta);
    end
end
