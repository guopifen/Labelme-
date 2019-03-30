%%
clear all
path='C:\Users\Lsk\Desktop\RGB_N\matlab\提取坐标\masks';%加载指定的数据,因为我把二值化后的图像都保存在了mat中
files=dir(fullfile(path, strcat('*', '.png')));
for i = 1:length(files)
%     Process_data= size(Z(i).imageCroped,2);
%     if Process_data == 6  %当鱼的数量等于6时，继续执行
        srcName = files(i).name;
        I=imread(fullfile(path, srcName));
        %I = Z(i).btnimage{1,1};%读入图像  这一步是关键，可以在此程序基础上修改，加载转换成二值化的图片
        BW = im2bw(I, graythresh(I));%转换成2进制图像
        BW=~BW;
        [B,L] = bwboundaries(BW,'noholes');%寻找边缘，不包括孔
        mid_arug = cell(length(B),2);
     for k = 1:length(B)%B 每条鱼对应的边界坐标
         boundary = B{k}; %boundary表示所有的轮廓坐标,为了节省内存，我们取其1/4
         x_coordinate =  boundary(1:4:end,2);%每条鱼边界的横坐标
         y_coordinate =  boundary(1:4:end,1);
         mid_arug{k,1} = {boundary(1:4:end,2)};
         mid_arug{k,2} = {boundary(1:4:end,1)};
     end
     assignin('base',['img_',num2str(i)],mid_arug);
%      save(['H:/' '/' ['img_',num2Rstr(i)] '.mat'],'mid_arug');
     save(['C:\Users\Lsk\Desktop\RGB_N\matlab\提取坐标\coordinate2\' srcName(1:end-4) '.mat'],'mid_arug');
%     end
end
