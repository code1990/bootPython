# Python OS 文件/目录方法
# os 模块提供了非常丰富的方法用来处理文件和目录
import os,sys,time
# 打开文件
path = "C:\\Users\\Administrator\\Desktop\\111.txt"
fd = os.open( path, os.O_RDWR|os.O_CREAT )
str="hello python"
# 检验权限模式 如果允许访问返回 True , 否则返回False。
print(os.access(path, os.F_OK))
# # 改变当前工作目录
# os.chdir(path)
# # 设置路径的标记为数字标记。
# os.chflags(path, flags)
# # 更改权限
# os.chmod(path)
# # 更改文件所有者
# os.chown(path, uid, gid)
# # 改变当前进程的根目录
# os.chroot(path)
# # 关闭文件描述符 fd
# os.close(fd)
# # 关闭所有文件描述符，从 fd_low (包含) 到 fd_high (不包含), 错误会忽略
# os.closerange(fd_low, fd_high)
# # 复制文件描述符 fd
# os.dup(fd)
# # 将一个文件描述符 fd 复制到另一个 fd2
# os.dup2(fd, fd2)
# # 通过文件描述符改变当前工作目录
# os.fchdir(fd)
# # 改变一个文件的访问权限，该文件由参数fd指定，参数mode是Unix下的文件访问权限。
# os.fchmod(fd)
# # 修改一个文件的所有权，这个函数修改一个文件的用户ID和用户组ID，该文件由文件描述符fd指定。
# os.fchown(fd, uid, gid)
# # 强制将文件写入磁盘，该文件由文件描述符fd指定，但是不强制更新文件的状态信息。
# os.fdatasync(fd)
# # 通过文件描述符 fd 创建一个文件对象，并返回这个文件对象
# os.fdopen(fd[[, bufsize]])
# # 返回一个打开的文件的系统配置信息。name为检索的系统配置的值，它也许是一个定义系统值的字符串，这些名字在很多标准中指定（POSIX.1, Unix 95, Unix 98, 和其它）。
# os.fpathconf(fd, name)
# # 返回文件描述符fd的状态，像stat()。
# os.fstat(fd)
# # 返回包含文件描述符fd的文件的文件系统的信息，像 statvfs()
# os.fstatvfs(fd)
# # 强制将文件描述符为fd的文件写入硬盘。
# os.fsync(fd)
# # 裁剪文件描述符fd对应的文件, 所以它最大不能超过文件大小。
# os.ftruncate(fd, length)
# # 返回当前工作目录
# os.getcwd()
# # 返回一个当前工作目录的Unicode对象
# os.getcwdu()
# # 如果文件描述符fd是打开的，同时与tty(-like)设备相连，则返回true, 否则False。
# os.isatty(fd)
# # 设置路径的标记为数字标记，类似 chflags()，但是没有软链接
# os.lchflags(path, flags)
# # 修改连接文件权限
# os.lchmod(path)
# # 更改文件所有者，类似 chown，但是不追踪链接。
# os.lchown(path, uid, gid)
# # 创建硬链接，名为参数 dst，指向参数 src
# os.link(src, dst)
# # 返回path指定的文件夹包含的文件或文件夹的名字的列表。
# os.listdir(path)
# # 设置文件描述符 fd当前位置为pos, how方式修改: SEEK_SET 或者 0 设置从文件开始的计算的pos; SEEK_CUR或者 1 则从当前位置计算; os.SEEK_END或者2则从文件尾部开始. 在unix，Windows中有效
# os.lseek(fd, pos, how)
# # 像stat(),但是没有软链接
# os.lstat(path)
# # 从原始的设备号中提取设备major号码 (使用stat中的st_dev或者st_rdev field)。
# os.major(device)
# # 以major和minor设备号组成一个原始设备号
# os.makedev(major, minor)
# # 递归文件夹创建函数。像mkdir(), 但创建的所有intermediate-level文件夹需要包含子文件夹。
# os.makedirs(path[])
# # 从原始的设备号中提取设备minor号码 (使用stat中的st_dev或者st_rdev field )。
# os.minor(device)
# # 以数字mode的mode创建一个名为path的文件夹.默认的 mode 是 0777 (八进制)。
# os.mkdir(path[])
# # 创建命名管道，mode 为数字，默认为 0666 (八进制)
# os.mkfifo(path[])
# # 创建一个名为filename文件系统节点（文件，设备特别文件或者命名pipe）。
# os.mknod(filename[=0600, device])
# # 打开一个文件，并且设置需要的打开选项，mode参数是可选的
# os.open(file, flags[])
# # 打开一个新的伪终端对。返回 pty 和 tty的文件描述符。
# os.openpty()
# # 返回相关文件的系统配置信息。
# os.pathconf(path, name)
# # 创建一个管道. 返回一对文件描述符(r, w) 分别为读和写
# os.pipe()
# # 从一个 command 打开一个管道
# os.popen(command[[, bufsize]])
# # 从文件描述符 fd 中读取最多 n 个字节，返回包含读取字节的字符串，文件描述符 fd对应文件已达到结尾, 返回一个空字符串。
# os.read(fd, n)
# # 返回软链接所指向的文件
# os.readlink(path)
# # 删除路径为path的文件。如果path 是一个文件夹，将抛出OSError; 查看下面的rmdir()删除一个 directory。
# os.remove(path)
# # 递归删除目录。
# os.removedirs(path)
# # 重命名文件或目录，从 src 到 dst
# os.rename(src, dst)
# # 递归地对目录进行更名，也可以对文件进行更名。
# os.renames(old, new)
# # 删除path指定的空目录，如果目录非空，则抛出一个OSError异常。
# os.rmdir(path)
# # 获取path指定的路径的信息，功能等同于C API中的stat()系统调用。
# os.stat(path)
# # 决定stat_result是否以float对象显示时间戳
# os.stat_float_times([newvalue])
# # 获取指定路径的文件系统统计信息
# os.statvfs(path)
# # 创建一个软链接
# os.symlink(src, dst)
# # 返回与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组
# os.tcgetpgrp(fd)
# # 设置与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组为pg。
# os.tcsetpgrp(fd, pg)
# # 返回唯一的路径名用于创建临时文件。
# os.tempnam([dir[, prefix]])
# # 返回一个打开的模式为(w+b)的文件对象 .这文件对象没有文件夹入口，没有文件描述符，将会自动删除。
# os.tmpfile()
# # 为创建一个临时文件返回一个唯一的路径
# os.tmpnam()
# # 返回一个字符串，它表示与文件描述符fd 关联的终端设备。如果fd 没有与终端设备关联，则引发一个异常。
# os.ttyname(fd)
# # 删除文件路径
# os.unlink(path)
# # 返回指定的path文件的访问和修改的时间。
# os.utime(path, times)
# # 输出在文件夹中的文件名通过在树中游走，向上或者向下。
# os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])
# # 写入字符串到文件描述符 fd中. 返回实际写入的字符串长度
# os.write(fd, str)
# # 获取文件的属性信息。
# print(os.path())

# Python os.path() 模块
# os.path 模块主要用于获取文件的属性。

print(os.path.basename('/runoob.txt'))  # 返回文件名
print(os.path.dirname('/runoob.txt'))  # 返回目录路径
print(os.path.split('/runoob.txt'))  # 分割文件名与路径
print(os.path.join('root', 'test', 'runoob.txt'))  # 将目录和文件名合成一个路径

file = 'C:\\Users\\Administrator\\Desktop\\111.txt'  # 文件路径

print(os.path.getatime(file))  # 输出最近访问时间
print(os.path.getctime(file))  # 输出文件创建时间
print(os.path.getmtime(file))  # 输出最近修改时间
print(time.gmtime(os.path.getmtime(file)))  # 以struct_time形式输出最近修改时间
print(os.path.getsize(file))  # 输出文件大小（字节为单位）
print(os.path.abspath(file))  # 输出绝对路径
print(os.path.normpath(file))  # 规范path字符串形式