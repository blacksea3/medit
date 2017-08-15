//编辑板块
//标题不能为空 标题备注限制50字符、描述限制100字符、字符任意。
//1个汉字为1个字符

$(function(){
	$('.skin-minimal input').iCheck({
		checkboxClass: 'icheckbox-blue',
		radioClass: 'iradio-blue',
		increaseArea: '20%'
	});
	
	//表单验证
	$("#form-article-edit").validate({
		//注意：这里这些形如blocktitle的标记是form里面的name,不是id!!!
		rules:{
			articletitle:{
				required:true,
				maxlength:50,
			},
			articlecontent:{
				required:true,
			},
			articleremark:{
				maxlength:50,
			},			
		},
		onkeyup:false,
		focusInvalid:true,
		success:"valid",
		submitHandler:function(form)
		{
			$.ajax({
				url: "../article-edit/", async: true,           
					data:
					{
						aid: $("#articleid").text(),
						title: $("#articletitle").val(),
						content: CKEDITOR.instances.articlecontent.getData(),
						blockid: $("#articlecolumn option:selected").val(),
						remark: $("#articleremark").val(),
						csrfmiddlewaretoken:$("#form-article-edit").find("input[name='csrfmiddlewaretoken']").val()
					}, success:
					function (data) {
						if(data == 'T')
						{
							alert('修改成功');
							removeIframe();
						}
						else
						{
							alert('服务器内部错误！');
						}
					}, type: "POST"
			});
		}
	});

	state = "pending";
});

function removeIframe()
{
	var index = parent.layer.getFrameIndex(window.name);  
	parent.layer.close(index); 
};