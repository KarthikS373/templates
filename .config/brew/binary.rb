# @binaryBrew [PythonCli](https://github.com/megabyte-labs/template-python-cli) - Boilerplate/Template for Python CLI projects
class PythonCli < Formula
  desc "Boilerplate/Template for Python CLI projects"
  homepage "https://megabyte.space"
  url "https://github.com/megabyte-labs/template-python-cli/releases/download/v1.1.14/python-cli.tar.gz"
  version "1.1.14"
  license "MIT"

  

  def install
    os = OS.kernel_name.downcase
    arch = Hardware::CPU.intel? ? "amd64" : Hardware::CPU.arch.to_s
    bin.install "build/python-cli-#{os}_#{arch}" => "python-cli"
  done

  test do
    system bin/"python-cli", "--version"
  end
end
