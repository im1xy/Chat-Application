#pragma once
#include <fstream>
#include <cstdlib>
#include <msclr\marshal_cppstd.h>

extern "C" __declspec(dllexport) void login();

namespace CLogin {

	using namespace System;
	using namespace System::ComponentModel;
	using namespace System::Collections;
	using namespace System::Windows::Forms;
	using namespace System::Data;
	using namespace System::Drawing;

	/// <summary>
	/// Summary for Login
	/// </summary>
	public ref class Login : public System::Windows::Forms::Form
	{
	public:
		Login(void)
		{
			InitializeComponent();
			//
			//TODO: Add the constructor code here
			//
		}

	protected:
		/// <summary>
		/// Clean up any resources being used.
		/// </summary>
		~Login()
		{
			if (components)
			{
				delete components;
			}
		}
	private: System::Windows::Forms::Label^ top_label;
	private: System::Windows::Forms::Button^ login_button;
	private: System::Windows::Forms::Button^ cancel_button;
	protected:

	private: System::Windows::Forms::TextBox^ input;
	private: System::Windows::Forms::Label^ welcome_label;
	private: System::Windows::Forms::Label^ ErrorLabel;
	protected:

	private:
		/// <summary>
		/// Required designer variable.
		/// </summary>
		System::ComponentModel::Container ^components;

#pragma region Windows Form Designer generated code
		/// <summary>
		/// Required method for Designer support - do not modify
		/// the contents of this method with the code editor.
		/// </summary>
		void InitializeComponent(void)
		{
			this->top_label = (gcnew System::Windows::Forms::Label());
			this->login_button = (gcnew System::Windows::Forms::Button());
			this->cancel_button = (gcnew System::Windows::Forms::Button());
			this->input = (gcnew System::Windows::Forms::TextBox());
			this->welcome_label = (gcnew System::Windows::Forms::Label());
			this->ErrorLabel = (gcnew System::Windows::Forms::Label());
			this->SuspendLayout();
			// 
			// top_label
			// 
			this->top_label->AutoSize = true;
			this->top_label->BackColor = System::Drawing::Color::Transparent;
			this->top_label->Font = (gcnew System::Drawing::Font(L"Roboto Mono", 13, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(204)));
			this->top_label->ForeColor = System::Drawing::Color::White;
			this->top_label->Location = System::Drawing::Point(10, 152);
			this->top_label->Margin = System::Windows::Forms::Padding(4, 0, 4, 0);
			this->top_label->Name = L"top_label";
			this->top_label->Size = System::Drawing::Size(415, 34);
			this->top_label->TabIndex = 0;
			this->top_label->Text = L"How should you be called\?\r\n";
			// 
			// login_button
			// 
			this->login_button->BackColor = System::Drawing::Color::MediumSlateBlue;
			this->login_button->Font = (gcnew System::Drawing::Font(L"Roboto Mono", 10, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(204)));
			this->login_button->ForeColor = System::Drawing::Color::White;
			this->login_button->Location = System::Drawing::Point(16, 296);
			this->login_button->Margin = System::Windows::Forms::Padding(4);
			this->login_button->Name = L"login_button";
			this->login_button->Size = System::Drawing::Size(124, 57);
			this->login_button->TabIndex = 1;
			this->login_button->Text = L"Login";
			this->login_button->UseVisualStyleBackColor = false;
			this->login_button->Click += gcnew System::EventHandler(this, &Login::login_button_Click);
			// 
			// cancel_button
			// 
			this->cancel_button->BackColor = System::Drawing::Color::MediumSlateBlue;
			this->cancel_button->Font = (gcnew System::Drawing::Font(L"Roboto Mono", 10, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(204)));
			this->cancel_button->ForeColor = System::Drawing::Color::White;
			this->cancel_button->Location = System::Drawing::Point(291, 296);
			this->cancel_button->Margin = System::Windows::Forms::Padding(4);
			this->cancel_button->Name = L"cancel_button";
			this->cancel_button->Size = System::Drawing::Size(124, 57);
			this->cancel_button->TabIndex = 2;
			this->cancel_button->Text = L"Cancel";
			this->cancel_button->UseVisualStyleBackColor = false;
			this->cancel_button->Click += gcnew System::EventHandler(this, &Login::cancel_button_Click);
			// 
			// input
			// 
			this->input->BackColor = System::Drawing::Color::DarkSlateBlue;
			this->input->CausesValidation = false;
			this->input->Font = (gcnew System::Drawing::Font(L"Roboto Mono", 13, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(204)));
			this->input->ForeColor = System::Drawing::Color::White;
			this->input->Location = System::Drawing::Point(16, 222);
			this->input->Margin = System::Windows::Forms::Padding(4);
			this->input->MaxLength = 13;
			this->input->Name = L"input";
			this->input->Size = System::Drawing::Size(399, 42);
			this->input->TabIndex = 3;
			this->input->TextAlign = System::Windows::Forms::HorizontalAlignment::Center;
			// 
			// welcome_label
			// 
			this->welcome_label->AutoSize = true;
			this->welcome_label->BackColor = System::Drawing::Color::Transparent;
			this->welcome_label->FlatStyle = System::Windows::Forms::FlatStyle::Flat;
			this->welcome_label->Font = (gcnew System::Drawing::Font(L"Roboto Mono", 16, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(204)));
			this->welcome_label->ForeColor = System::Drawing::Color::White;
			this->welcome_label->Location = System::Drawing::Point(134, 43);
			this->welcome_label->Margin = System::Windows::Forms::Padding(4, 0, 4, 0);
			this->welcome_label->Name = L"welcome_label";
			this->welcome_label->Size = System::Drawing::Size(152, 43);
			this->welcome_label->TabIndex = 4;
			this->welcome_label->Text = L"Welcome";
			// 
			// ErrorLabel
			// 
			this->ErrorLabel->AutoSize = true;
			this->ErrorLabel->Font = (gcnew System::Drawing::Font(L"Roboto Mono", 12, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(204)));
			this->ErrorLabel->ForeColor = System::Drawing::Color::White;
			this->ErrorLabel->Location = System::Drawing::Point(146, 307);
			this->ErrorLabel->Name = L"ErrorLabel";
			this->ErrorLabel->Size = System::Drawing::Size(0, 32);
			this->ErrorLabel->TabIndex = 5;
			// 
			// Login
			// 
			this->AutoScaleDimensions = System::Drawing::SizeF(12, 26);
			this->AutoScaleMode = System::Windows::Forms::AutoScaleMode::Font;
			this->BackColor = System::Drawing::Color::DarkSlateBlue;
			this->BackgroundImageLayout = System::Windows::Forms::ImageLayout::Stretch;
			this->ClientSize = System::Drawing::Size(432, 367);
			this->Controls->Add(this->ErrorLabel);
			this->Controls->Add(this->welcome_label);
			this->Controls->Add(this->input);
			this->Controls->Add(this->cancel_button);
			this->Controls->Add(this->login_button);
			this->Controls->Add(this->top_label);
			this->Font = (gcnew System::Drawing::Font(L"Roboto Mono", 10, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(204)));
			this->FormBorderStyle = System::Windows::Forms::FormBorderStyle::None;
			this->Margin = System::Windows::Forms::Padding(4);
			this->Name = L"Login";
			this->StartPosition = System::Windows::Forms::FormStartPosition::CenterScreen;
			this->Text = L"Login";
			this->ResumeLayout(false);
			this->PerformLayout();

		}
#pragma endregion
	private: System::Void cancel_button_Click(System::Object^ sender, System::EventArgs^ e) {
		this->Close();
	}
	private: System::Void login_button_Click(System::Object^ sender, System::EventArgs^ e) {
		if (this->input->Text == "")
		{
			this->ErrorLabel->Text = "Try Again";
			return;
		}

		std::string username = msclr::interop::marshal_as<std::string>(this->input->Text);

		std::string file_path(std::getenv("USERPROFILE"));
		std::string file_name = "\\login_data.txt";
		file_path += file_name;

		std::ofstream out(file_path);
		out << username;
		out.close();
		this->Close();
	}
};
}


