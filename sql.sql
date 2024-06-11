/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 8.0.21 : Database - local_area_taxi
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`local_area_taxi` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `local_area_taxi`;

/*Data for the table `category` */

insert  into `category`(`id`,`category`) values 
(2,'Car-Taxi'),
(3,'Jeap-Taxi');

/*Data for the table `complaint` */

insert  into `complaint`(`cid`,`complaint`,`cdate`,`user_id`,`reply`,`rdate`) values 
(1,'bad','2021-04-01',4,'pending','0000-00-00');

/*Data for the table `driver` */

insert  into `driver`(`driver_id`,`name`,`age`,`place`,`post`,`pin`,`district`,`latitude`,`longitude`,`image`,`phone`,`email`,`licence_no`) values 
(2,'Ram',36,'kallar','rajapuram',671532,'kannur',11.8687821,75.3643547,'/static/210401-092935.jpg',7902241032,'soumyakrishnan210@gmail.com','1'),
(5,'abc',36,'Padanapalam','kannur',671001,'kannur',11.8686863,75.3625331,'/static/210408-085829.jpg',9632580741,'soumyakrishnankallar@gmail.com','90'),
(6,'a',56,'Padanapalam','kannur',789654,'kannur',11.8686863,75.3625331,'/static/210408-090143.jpg',8963257410,'abc@gmail.com','67'),
(7,'sr',24,'Kannur','kk',678678,'knr',11.8717139,75.3607114,'/static/210409-220648.jpg',6969696969,'sr@gmail.com','224555'),
(8,'Soumya',21,'Kannur','kallar',876430,'Kasaragod',11.8686863,75.3625331,'/static/210417-133821.jpg',9632580741,'soumyakrishnan@gmail.com','855');

/*Data for the table `feedback` */

insert  into `feedback`(`fid`,`user_id`,`feedback`,`date`) values 
(1,4,'very bad','2021-04-01'),
(2,4,'dft','2021-04-08'),
(3,4,'baa','2021-04-15');

/*Data for the table `location` */

insert  into `location`(`id`,`driver_id`,`latitude`,`longitude`,`place`) values 
(1,2,0,0,''),
(2,6,11.8686863,75.3625331,'Kannur'),
(3,7,11.8673939,75.3643547,'Kannur'),
(4,8,11.8686863,75.3625331,'Kannur');

/*Data for the table `login` */

insert  into `login`(`login_id`,`user_name`,`password`,`user_type`) values 
(2,'abc','123','driver'),
(1,'admin','admin','admin'),
(4,'xyz','abc','user'),
(5,'aaa','12','rejected'),
(6,'x','x','driver'),
(7,'sr','sr','driver'),
(8,'soumya','123','pending'),
(9,'sss','ss','user');

/*Data for the table `rating` */

insert  into `rating`(`rate_id`,`rate`,`user_id`,`date`) values 
(1,3,4,'2021-04-01'),
(2,4,4,'2021-04-08'),
(3,4,4,'2021-04-08');

/*Data for the table `request` */

insert  into `request`(`request_id`,`user_id`,`driver_id`,`date&time`,`status`,`latitude`,`longitude`,`place`) values 
(1,4,7,'2021-04-17 12:23:19','accepted',11.8673939,75.3643547,'Kannur');

/*Data for the table `user` */

insert  into `user`(`user_id`,`user_name`,`gender`,`place`,`post`,`pin`,`district`,`phone`,`email`) values 
(4,'soumya','FEMALE','kallar','kallar',310987,'Kasaragod',9632580741,'soumya@gmail.com'),
(9,'soumya','FEMALE','kallar','kallar',876543,'Kasaragod',9632580741,'aaa@gmail.com');

/*Data for the table `vehicle` */

insert  into `vehicle`(`vehicle_id`,`driver_id`,`vehicle_type`,`vehicle_no`,`available_seats`,`category_id`) values 
(1,2,'car','123',4,1),
(3,6,'car','5',6,2),
(4,7,'car','1000',6,2);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
