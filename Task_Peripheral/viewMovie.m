function [] = viewMovie(path)
    dataMatrix = load(path);
    names = fieldnames(dataMatrix);
    name = names{1};
    dataMatrix = dataMatrix.(name);
    [x, y, t] = size(dataMatrix);
    figure;
    colormap('gray');
    for i=1:t
        title(strcat('frame', num2str(i)));
        imagesc(dataMatrix(:, :, i));
        hold on;
        pause(0.05)
    end
end