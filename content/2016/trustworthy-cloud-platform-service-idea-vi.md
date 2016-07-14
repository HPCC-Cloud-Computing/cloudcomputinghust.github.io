Title: Ý tưởng nền tảng an toàn Đám mây
Slug: trustworthy-cloud-platform-service-idea
Date: 2016-05-21 11:26
Author: Giáp Trần
Tags: keystone,federation,security
Translator: Giap Tran
Lang: vi
Status: published

# Bảo mật trong Đám mây

## Mở đầu

Cloud, nó không chỉ là một khái niệm. Cloud là một nền tảng được đề cập và phát triển mạnh mẽ trong những năm gần đây. Một trang website đơn giản hay bất kỳ dịch vụ phức tạp nào trên Internet mà bạn đã đang sử dụng. Nó rất có thể đang chạy trên nền tảng Cloud.

Khi mà có rất nhiều ứng dụng, dịch vụ trên cloud. Ngoài việc sức mạnh mà cloud mang lại.
Vấn đề bảo mật thông tin và an toàn dịch vụ trên Cloud như thế nào?

## THỐNG KÊ NĂM 2015
### Ứng dụng Cloud

![apps-cloud.png](http://cloudcomputinghust.github.io/images/apps-cloud.png)

- Ứng dụng web chiếm 43%
- Ứng dụng truyền thông chiếm 39%
- Bán hàng và quảng cáo chiếm 30%

### Dữ liệu trong Cloud
Dữ liệu Email được các công ty lưu trữ  thường xuyên nhiều nhất (45%). Tiếp theo là dữ liệu bán hàng của công ty (42%). Các sản phẩm trí truệ (38%) và các thông tin khách hàng với 31%.

Rất ít thông tin về tài chính (19%) và dữ liệu chăm sóc sức khoẻ của nhân viên(8%).

![data-cloud.png](http://cloudcomputinghust.github.io/images/data-cloud.png)

## BÀI TOÁN
Khi Cloud mới xuất hiện, các bài toán về hiệu năng, tính sẵn sàng,... được quan tâm hàng đầu. Và khi Cloud đã trờ thành nền tảng, công cụ của các công ty, người dùng. Vấn đề an toàn thông tin được đặt lên hàng đầu.

Nhiều giải pháp được đưa ra để hạn chế, ngăn chặn việc truy cập trái phép từ các tác nhân (hacker ) bên ngoài.

Nhưng, dữ liệu có bảo mật đối với bên cung cấp dịch vụ Cloud (bên trong Cloud)???
Liệu có tồn tại nguy cơ mất an toàn bảo mật: từ cơ sở hạ tầng, từ môi trường mạng, từ các nhân viên, từ những khách hàng khác,... xuất phát bên trong nhà cung cấp???

**_“Có tin tưởng khi giao dữ liệu nhạy cảm cho một bên khác?”_**

Đây là mối quan tâm chính cho các công ty đang tham gia các cơn sốt vàng đó là Cloud Computing.
Cách phổ biến nhất để thiết lập sự tin tưởng giữa một Cloud User (Data Controllers)  và một nhà cung cấp Cloud (Data Processors) là phải xây dựng một Hiệp định mức độ dịch vụ (SLA) và kiểm toán.

![issue.png](http://cloudcomputinghust.github.io/images/issue.png)

** Ngay cả khi các nhà cung cấp đám mây được kiểm toán, tình hình hiện nay chỉ ra một số nguy cơ bảo mật nghiêm trọng: **

1. Ngay sau khi các hoạt động CNTT được đưa vào Cloud thì người dùng mất kiểm soát nó.
Ví du: nếu dữ liệu đã upload lên Cloud (hay vào trong một máy ảo Cloud) nhà cung cấp luôn luôn có thể truy cập và chỉnh sửa nó.
2. Ngay cả khi nhà cung cấp ràng buộc bởi SLA thì vẫn tiềm ẩn mối đe doạ tiết lộ thông tin nhạy cảm của khách hàng và tính toán trong Cloud. Đặc biệt bởi các nội bộ bên trong (ví dụ: người kỹ thuật Cloud ).
3. An ninh cở sở hạ tầng, phầm mềm của nhà cung cấp đám mây liệu có đảm bảo?

**Để giải quyết được các vấn đề an ninh này, chúng ta cần giải quyết được bài toán sau:**

_“Làm thế nào để người dùng được phép sử dụng tài nguyên đám mây mà không tiết lộ các thông tin nhạy cảm (dữ liệu, ứng dụng / chức năng / quy trình) cho các nhà cung cấp đám mây nhưng đồng thời lại cho phép các nhà cung cấp đám mây để quản lý cơ sở hạ tầng đám mây an toàn và có hiệu quả?”_

## Ý TƯỞNG
![idea.png](http://cloudcomputinghust.github.io/images/idea.png)

- Cloud User:

Không đưa dữ liệu chứng thực trực tiếp với nhà cung cấp đám mây.

- Cloud Provider:

Không biết dữ liệu mà mình đang quản lý là của những cá nhân hay tổ chức nào.

- Trust Sevice:

 **Đối với phía User:**
Dịch vụ mà người dùng tin cậy để cung cấp các thông tin cá nhân, và thông qua agent để sử dụng cloud được cung cấp từ phía provider, mà không cần biết Cloud này là của Provider nào.
 **Đối với phía Provider:**
Không được biết khách hàng của mình là ai, tất cả khách hàng sẽ được Agent chuyển giao bằng một định dang nào đó.

![idea-1.png](http://cloudcomputinghust.github.io/images/idea-1.png)
