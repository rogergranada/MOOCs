function [y_out] = laff_copy( x,y )

[rows_x, cols_x] = size(x);
[rows_y, cols_y] = size(y);

% make sure x and y are at least vectors
if (rows_x ~=1 && cols_x ~= 1) || (rows_y ~= 1 && cols_y ~= 1)
    y_out = 'FAILED';
    return 
end

% make sure they are both the same size
if (rows_x * cols_x ~= rows_y * cols_y)
    y_out = 'FAILED';
    return
end

% now we copy x and to y. Use nested ifs, because we need to handle 
% the case where one is a column vector, and one is a row vector.
if (cols_x == 1) % column vector
    if (cols_y == 1) % y is also a column vector
        for i = 1:rows_x
            y(i,1) = x(i,1); % just do a straight copy
        end
    else % y is a row vector so we must transpose
        for i = 1:rows_x
            y(1,i) = x(i,1);
        end
    end
else % x is a row vector
    if (cols_y == 1) % but y is not, so transpose
        for i = 1:cols_x
            y(i,1) = x(1,i);
        end
    else % y is a row vector, so just copy straight copy
        for i = 1:cols_x
            y(1,i) = x(1,i);
        end
    end
end

y_out = y;

return

end
