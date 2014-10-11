% dot plot
s1 = 'MVHWTAEEKQLITGLWGKVNVAECGAEALARLLIVYPWTQRFFASFGNLSSPTAILGNPMVRAHGKKVLTSFGDAVKNLDNIKNTFSQLSELHCDKLHVDPENFRLLGDILIIVLAAHFSKDFTPECQAAWQKLVRVVAHALARKYH';
s2 = 'MVHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYH';
[m, ind1] = max([length(s1), length(s2)]);
[n, ind2] = min([length(s1), length(s2)]);
if ind1 == 1
    A = s1;
    B = s2;
else
    B = s1;
    A = s2;
end
dot = zeros([m, n]);
x_axis = zeros(m, 1);
y_axis = zeros(n, 1);
for i=1:m
    for j=1:m
        if A(i) == B(j)
%             x_axis(i,1) = i;
%             y_axis(j,1) = j;
              dot(i, j) = j;
        end
    end
end

plot(dot,'.b')

z = 0;
for c=-m:n
    z = z + 1;
    val(z) = 0;
    for i=1:m
        if (i-c > 0) && (i-c <= m)
            if dot(i,i-c) > 0
                val(z) = val(z) + 1;
            end
        end
    end
end

[temp, inter] = max(val);
l = -m:n;
c = l(inter);
align = '';

for i=1:m
    if dot(i, i) > 0
        align = cat(2,align,s1(i));
    else
        align = cat(2,align,'x');
    end
end

align