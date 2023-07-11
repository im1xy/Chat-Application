#include "Login.h"

using namespace System;
using namespace System::Windows::Forms;

extern "C" __declspec(dllexport) void login()
{
	Application::EnableVisualStyles();
	Application::SetCompatibleTextRenderingDefault(false);
	CLogin::Login loginform;

	loginform.ShowDialog();
}