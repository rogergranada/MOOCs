function [alpha_out] = laff_norm2(x)
    [rows_x, cols_x] = size(x);
    
    if ~isvector(x)
        alpha_out = 'FAILED';
        return
    end
    
    alpha = 0;
    
    if (cols_x == 1) % we have a column vector
        for i = 1:rows_x
            alpha = alpha + x(i,1) * x(i,1);
        end
    else
        for i = 1:cols_x
            alpha = alpha + x(1,i) * x(1,i);
        end
    end
    
    alpha_out = sqrt(alpha);
end
