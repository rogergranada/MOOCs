function [y_out] = laff_axpy(alpha, x, y)
  
    [rows_x, cols_x] = size(x);
    [rows_y, cols_y] = size(y);
    
    if ~isscalar(alpha)
        y_out = 'FAILED';
        return
    end
    
    if ~isvector(x)
        y_out = 'FAILED';
        return
    end
    
    if ~isvector(y)
        y_out = 'FAILED';
        return
    end
    
    if (cols_x * rows_x ~= cols_y * rows_y)
        y_out = 'FAILED';
        return
    end
    
    if (cols_x == 1) % we have a column vector
        if (cols_y == 1) 
            for i = 1:rows_x
                y(i,1) = alpha * x(i,1) + y(i,1); % col - col
            end
        else
            for i = 1:rows_x
                y(1,i) = alpha * x(i,1) + y(1,i); % col - row
            end
        end 
    else
        if (cols_y == 1)
            for i = 1:cols_x
                y(i,1) = alpha * x(1,i) + y(i,1); % row - col 
            end
        else
            for i = 1:cols_x
                y(1,i) = alpha * x(1,i) + y(1,i); % row - row
                    
            end
        end
    end
    
    y_out = y;
end
