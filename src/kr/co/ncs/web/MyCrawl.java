package kr.co.ncs.web;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

@WebServlet("/mycrawl")
public class MyCrawl extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		response.setContentType("text/html; charset=UTF-8");
		response.setCharacterEncoding("utf-8");
		try {
			//object 타입 toString으로 형변환
			HttpSession session = request.getSession();
			String name = session.getAttribute("user_name").toString();
//			response.getWriter().append(name);
			response.getWriter().append("<table border=1><tr><td>sujin</td><td>123-1234-1234</td></tr></table>");
			
		}catch(Exception e){
			response.getWriter().append("you have no authority for this page");
		}
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	}

}
